#!/usr/bin/env io

KUIWidget := Object clone do (
	/* parent & children here are used only for layout */
	parent := nil
	children := List clone

	bbox := Box clone
	parentcenter := Point clone
	center := Point clone
	offset := Point clone
	
	zlayer := 0

	img := Image clone
	img size := method(
		return Point clone set(width, height)
	)
	_calculateBbox := method(
		e := try(
			parentBbox := parent bbox
		)
		e catch (
			parentBbox := Box clone set(Point clone, Point clone)
		)
		bboxOrigin := ((parentBbox origin) + ((parentBbox size)*(parentcenter))) + offset
		bboxSize := Point clone set (img width, img height)
		self bbox := Box clone set(bboxOrigin, bboxSize)
		?widgetLint
		return bbox
	)
	
	size := method( return bbox size )
	
	_calculateSize := method ( return size )
	
	calculateBbox := method(
		_calculateBbox
		children foreach(c, c ?calculateBbox)
	)
	calculateSize := method(
		children foreach(c, c ?calculateSize)
		return _calculateSize
	)
	setParent := method(p, 
		self parent := p
		p children append(self)
	)
)
KUIContainer := KUIWidget clone do (
	widgetLint := method(
		if(children size < 1,
			children foreach(c, 
				if(c zlayer <= zlayer, c zlayer := (zlayer + 1))
			)
			children foreach(c, c ?widgetLint)
			children foreach(c, 
				self bbox := bbox Union(c bbox)
			)
		)
		return bbox
	)
)

