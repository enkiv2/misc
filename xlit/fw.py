#!/usr/bin/env python

# LEGAL NOTE:
# While I have written FloatingWorld implementations officially for Project Xanadu(tm), 
# this implementation shares no code with those. This code contains no material
# under trade secret protection related to Project Xanadu(tm).
#
# This code is inspired by, but not identical with, the FloatingWorld / ZZOGL system used
# by XanaduSpace and XanaSpace

from ZZCell import cells as homeSlice
from ZZCell import ZZCell

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
  def __mul__(self, o)
	  n=min(self.n, len(o))
	  ret=[0]*n
		for i in range(0, n):
		  ret[i]=self.coords[i]*o.coords[i]
		return ret

ORIGIN = Vector((0, 0))

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
  def getAttr(self, name, default=ORIGIN):
	  val = self.cell.getNext('fw.'+name)
		if val:
		  return val.getValue()
		return default
  def setAttr(self, name, value):
	  self.cell.setNext('fw.'+name, value)
  def __getattr__(self, name):
	  defaults = self.__class__.PROPERTY_DEFAULTS
	  if name in defaults:
		  return self.getAttr(name, defaults[name])
		raise AttributeError()
  def _render(self, screen):
	  pass
  def render(self, screen):
	  self._render(screen)
	  for child in self.children:
		  child.render(screen)
  @property
  def bbox(self):
	  return [self.pos-(self.size*self.center), self.pos+(self.size*self.center)]
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
    return parent.pos+(parent.size*(parent.center-self.parentcenter))+self.delta-(self.size*self.center)

class Slab(FWObj):
  PROPERTY_DEFAULTS = {
	  "type": "slab",
		"size": ORIGIN,
		"center": ORIGIN,
		"parentcenter": ORIGIN,
		"delta": ORIGIN,
		"color": (255, 255, 255, 127),
		"outline_width": 0,
		"border_radius": 0,
	}
  def _render(self, screen):
	  pygame.draw.rect(screen, self.color, pygame.Rect(self.bbox), self.outline_width, self.border_radius)

class Beam(FWObj):
  PROPERTY_DEFAULTS = {
	  "type": "beam",
		"size": ORIGIN,
		"center": ORIGIN,
		"parentcenter": ORIGIN,
		"delta": ORIGIN,
		"color": (127, 255, 127, 127),
		"endsets": [],
		"bookmark_width": 5,
	}
  def _render(self, screen):
	  endset_bboxes=[]
		for endset in self.endsets:
		  endset_bboxes.append(endset.bbox)
		coords = []
		if len(endset_bboxes) == 1:
		  end = ((bbox[1][1], bbox[0][0]), (bbox[1][1], bbox[1][1]))
		  coords = [end[0], (Vector(end[0])+Vector([self.bookmark_width, self.bookmark_width])).coords, (Vector(end[1]+Vector([self.bookmark_width, self.bookmark_width])).coords, end[1]]
		elif len(endset_bboxes) == 2:
		  (first, second) = (endset_bboxes[0], endset_bboxes[1])
			if second[0][0]<first[1][0]:
			  (first, second) = (second, first)
		  coords = [(first[1][0], first[1][1]), (
	  pygame.draw.polygon(screen, self.color, coords)

