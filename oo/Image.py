#!/usr/local/bin/python3
"""
>>> import os
>>> import tempfile
>>> border_color = "#FF0000"
>>> square_color = "#0000FF"
>>> img = os.path.join(tempfile.gettempdir(), "test.img")
>>> xpm = os.path.join(tempfile.gettempdir(), "test.xpm")
>>> width, height = 240, 60
>>> midx, midy = width // 2, height // 2
>>> image = Image(width, height, img)
>>> for x in range(width):
... 	for y in range(height):
... 		if x < 5 or x >= width - 5 or y < 5 or y >= height - 5:
... 			image[x, y] = border_color
... 		elif midx - 20 < x < midx + 20 and midy - 20 < y < midy + 20:
... 			image[x, y] = square_color
>>> image.save()
>>> image.export("square_eye.xpm")

"""

import os, pickle

USE_GETATTR = False

class ImageError(Exception): pass
class CoordinateError(Exception): pass
class LoadError(Exception): pass
class SaveError(Exception): pass
class ExportError(Exception): pass
class NoFilenameError(Exception): pass


class Image:
	def __init__(self, width, height, filename="", background="#FFFFFF"):
		self.filename = filename
		self.__background = background
		self.__data = {}
		self.__width = width
		self.__height = height
		self.__colors = {self.__background}

	@property
	def background(self):
		return self.__background

	@property
	def width(self):
		return self.__width

	@property
	def height(self):
		return self.__height

	@property
	def colors(self):
		return set(self.__colors)

	def __getitem__(self, coordinate):
		assert len(coordinate) == 2, "coordiante should be a 2-tuple"
		if(not(0 <= coordinate[0] < self.width) or
			not (0 <= coordinate[1] < self.height)):
			raise CoordinateError(str(coordinate))

		return self.__data.get(tuple(coordinate), self.__background)

	def __setitem__(self, coordinate, color):
		assert len(coordinate) == 2, "coordinate should be a 2-tuple"
		if(not(0 <= coordinate[0] < self.width) or
			not(0 <= coordinate[1] < self.height)):
			raise CoordinateError(str(coordinate))
		if color == self.__background:
			self.__data.pop(tuple(coordinate), None)
		else:
			self.__data[tuple(coordinate)]=color
			self.__colors.add(color)

	def __delitem__(self, coordinate):
		assert len(coordinate) == 2, "coordinate should be 2-tuple"
		if(not(0 <= coordinate[0] < self.width) or
			not(0 <= coordinate[1] < self.height)):
			raise CoordinateError(str(coordinate))
		self.__data.pop(tuple(coordinate), None)

	def save(self, filename=None):
		if filename is not None:
			self.filename = filename
		if not self.filename:
			raise NoFileNameError()	

		fh = None
		try:
			data = [self.width, self.height, self.__background, self.__data]
			fh = open(self.filename, "wb")
			pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
		except (EnvironmentError, pickle.UnpickingError) as err:
			raise SaveError(str(err))
		finally:
			if fh is not None:
				fh.close()

	def load(self, filename=None):
		if filename is not None:
			self.filename = filename
		if not self.filename:
			raise NoFileNameError()	
		
		fh = None
		try:
			fh = open(self.filename, "rb")
			pickle.load(fh)
			(self.__width, self.__height, self.__background, self.__data) = data
			self.__colors = (set(self.__data.values()) | {self.__background})
		except (EnvironmentError, pickle.UnpickingError) as err:
			raise SaveError(str(err))
		finally:
			if fh is not None:
				fh.close()

	def export(self, filename):
		if filename.lower().endswith(".xpm"):
			self.__export_xpm(filename)
		else:
			raise ExportError("unsupported export format: " + os.path.splitext(filename)[1])

	def __export_xpm(self, filename):
		name = os.path.splitext(os.path.basename(filename))[0]
		count = len(self.__colors)
		chars = [chr(x) for x in range(32, 127) if chr(x) != '"']
		if count > len(chars):
			chars = []
			for x in range(32, 127):
				if chr(x) == '"':
					continue
				for y in range(32, 127):
					if chr(y) == '"':
						continue
					chars.append(chr(x) + chr(y))
		chars.reverse()
		if count > len(chars):
			raise ExportError("cannot export XPM: too many colors")
		fh = None
		try:
			fh = open(filename, "w", encoding="ascii")
			fh.write("/* XPM */\n")
			fh.write("static char *{0}[] = {{\n".format(name))
			fh.write("/* columns rows colors chars-per-pixel */\n")
			fh.write('"{0.width} {0.height} {1} {2}",\n'.format(
				self, count, len(chars[0])))
			char_for_colour = {}
			for color in self.__colors:
				char = chars.pop()
				fh.write('"{char} c {color}",\n'.format(**locals()))
				char_for_colour[color] = char
			fh.write("/* pixels */\n")
			for y in range(self.height):
				row = []
				for x in range(self.width):
					color = self.__data.get((x, y), self.__background)
					row.append(char_for_colour[color])
				fh.write('"{0}",\n'.format("".join(row)))
			fh.write("};\n")
		except EnvironmentError as err:
			raise ExportError(str(err))
		finally:
			if fh is not None:
				fh.close()

if __name__ == "__main__":
	import doctest
	doctest.testmod()
