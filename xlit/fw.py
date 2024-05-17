#!/usr/bin/env python

# LEGAL NOTE:
# While I have written FloatingWorld implementations officially for Project Xanadu(tm), 
# this implementation shares no code with those. This code contains no material
# under trade secret protection related to Project Xanadu(tm).
#
# This code is inspired by, but not identical with, the FloatingWorld / ZZOGL system used
# by XanaduSpace and XanaSpace


class Vector:
  def __init__(self, coords):
	  if isinstance(coords, Vector):
		  self.coords
		else:
	    self.coords=coords
		  self.n=len(coords)
  def __len__(self):
	  return self.n
  def __add__(self, o):
	  n=min(self.n, len(o))
	  ret=[0]*n
		for i in range(0, n):
		  ret[i]=self.coords[i]+o.coords[i]
		return ret
  def __sub__(self, o):
	  n=min(self.n, len(o))
	  ret=[0]*n
		for i in range(0, n):
		  ret[i]=self.coords[i]-o.coords[i]
		return ret

ORIGIN = Vector((0, 0, 0))

class FWObj:
  PROPERTY_DEFAULTS = {
	  "type": "group",
		"size": ORIGIN,
		"center": ORIGIN,
		"parentcenter": ORIGIN,
		"delta": ORIGIN,
	}
  def __init__(self, cell):
	  self.cell=cell
  def _zz_get(self, name, default=ORIGIN):
	  val = self.cell.getNext('fw.'+name)
		if val:
		  return val.getValue()
		return default
  def __getattr__(self, name):
	  if name in defaults:
		  return self._zz_get(name, defaults[name])
		raise AttributeError()
  def render(self, screen):
	  for child in self.children:
		  child.render(screen)
  @property
	def children(self):
	  cells=[]
		c=self.cell.getNext('d.0')
		while c:
		  cells.append(FWObj(c))
			c=c.getNext('d.0')
		return cells
  @property
  def parent(self):
    return FWObj(self.cell.getNext('d.0', False))
  @property
  def pos(self):
    parent=self.parent
		coords=[0, 0, 0]
		for i in range(0, 3):
      coords[i]=parent.pos[i]+(parent.size[i]*(parent.center[i]-self.parentcenter[i]))+self.delta[i]-(self.size[i]*self.center[i])
  
