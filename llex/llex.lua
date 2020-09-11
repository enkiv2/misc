#!/usr/bin/env lua

function processPrelude(lines) 
	local ret={}
	local subst={}
	for linenum, line in ipairs(lines) do
		local idx=string.find(line, "\t")
		if "\t"==string.sub(line, 1, 1) then table.insert(ret, string.sub(line, 2))
		elseif idx~=nil and idx>1 then 
			subst["{"..string.sub(line, 1, idx-1).."}"]=string.sub(line, idx+1)
		else
			error("Invalid input in prelude, line "..linenum..": line must contain tab character!\n>> "..line)
		end
	end
	return ret, subst
end

function matchAny(line, pats)
	for _,pat in ipairs(pats) do
		if string.find(line, pat) then return true end
	end
	return false
end

function processRules(lines, subst)
	local ret={[[function llex(llexline)
	if false then print("dummy")]]}
	local accum={}

	local spats={}
	for k,v in pairs(subst) do table.insert(spats, k) end

	function addLastAccum() 
		-- add last accum, if it exists
		if #accum>0 then
			while #accum > 0 do
				table.insert(ret, "\t\t"..table.remove(accum, 1))
			end
			table.insert(ret, "\tend)")
		end
	end

	for linenum, line in ipairs(lines) do
		if "\t"==string.sub(line, 1, 1) then table.insert(accum, string.sub(line, 2))
		else
			addLastAccum()

			local idx=0
			local pattern=""
			local vars	=""
			idx=string.find(line, "\t")
			if idx and idx>1 then 
				pattern=string.sub(line, 1, idx-1)
				vars=string.sub(line, idx+1)
			else
				pattern=line
			end

			local ttl=50 -- we don't have an actual stack here, so we won't overrun lua's stack, but we should never loop forever
			while ttl>0 and matchAny(pattern, spats) do
				for p,q in pairs(subst) do  pattern=string.gsub(pattern, p, string.gsub(q, "%%", "%%%%"))	end
				ttl=ttl-1
			end
			
			if string.find(line, "\t") and string.find(line, "\t")>1 then 
				table.insert(ret, "\telseif string.match(llexline, [["..pattern.."]]) then llexline=string.gsub(llexline, [["..pattern.."]], function("..vars..")")
			else
				table.insert(ret, "\telseif string.match(llexline, [["..pattern.."]]) then llexline=string.gsub(llexline, [["..pattern.."]], function() ")
			end
		end
	end

	addLastAccum()
	table.insert(ret, [[
	else error("invalid syntax: "..llexline)
	end
	return llexline
end
function main() 
	local line=io.read("*line")
	while line do
		print(llex(line)) 
		line=io.read("*line")
	end
end
if arg then main() end]])
	return ret
end

function processAll(lines)
	local ret={}
	local subst={}
	local ret2={}

	local accum={}
	local phase=0
	function handlePhaseShift()
		phase=phase+1
		if phase==1 then
			ret2,subst = processPrelude(accum)
			table.insert(ret2, "-- end of prelude")
		elseif phase==2 then
			ret2=processRules(accum, subst)
			table.insert(ret2, "-- end of rules")
		else
			ret2=accum
		end
		accum={}
		while #ret2>0 do
			table.insert(ret, table.remove(ret2, 1))
		end
	end
	for _,line in ipairs(lines) do
		if(string.sub(line, 1, 2)=="%%") then 
			handlePhaseShift()
		else
			table.insert(accum, line)
			table.insert(ret, "-- LINE: "..line)
		end
	end

	handlePhaseShift()

	return ret
end

function main()
	local lines={}
	
	local line=io.read("*line")
	while line do
		table.insert(lines, line)
		line=io.read("*line")
	end

	local outlines=processAll(lines)

	for _,line in ipairs(outlines) do print(line) end

end

if arg ~= nil then main() end


