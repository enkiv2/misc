#!/usr/bin/env python

import gzip
import numpy as np

LabeledString = tuple[str, str]

k_cache={}
def k_complexity(value:str, label:str, memoize:bool = True) -> int:
		"""
		Estimate Kolmgorov complexity of a string using compression. Optionally, memoize these results.
		"""
		if memoize and label in k_cache:
				return k_cache[label]
		ret=len(gzip.compress(value.encode()))
		if memoize:
				k_cache[label]=ret
		return ret

def normalized_compression_distance(x:LabeledString, y:LabeledString) -> float:
		"""
		Normalized Compression Distance formula from Li, et al. (2004) as described in Jiang, et al. (2023)

		Args:
				x (LabeledString): a tuple consisting of a string and its label
				y (LabeledString): a tuple consisting of a string and its label

		Returns:
				number: the normalized compression distance between x and y
		"""
		Cx = k_complexity(*x)
		Cy = k_complexity(*y)
		xy = " ".join([x[0], y[0]])
		Cxy = k_complexity(xy, "", False)
		return Cxy - min(Cx, Cy) / max(Cx, Cy)


def lrtc(test_set:list[LabeledString], training_set:list[LabeledString], k:int = 2) -> list[str]:
		"""
		Low Resource Text Classifier, based on Jiang, et al. (2023)

		Args:
				test_set (array<tuple<str,str>>): the strings we are classifying
				training_set (array<tuple<str,str>>): the base corpus
				k (int): neighbour count for k-NN algorithm

		Returns:
				list<str>: an array of predicted classes (as the label for the nearest neighbour)
		"""
		ret=[]
		for x in test_set:
				distance_from_x = []
				for y in training_set:
						distance_from_x.append(normalized_compression_distance(x, y))
				sorted_idx = np.argsort(np.array(distance_from_x))
				top_k_class = list(training_set[sorted_idx[:k], 1])
				predict_class = max(set(top_k_class), key=top_k_class.count)
				ret.append(predict_class)
		return ret

def prettyprint_lrtc_matches(x, y, k=2):
		dy={}
		for item in y:
				dy[item[1]]=item[0]
		predict_classes = lrtc(x, y, k)
		for i, item in enumerate(x):
				print(item[0])
				print(f"\t{dy[predict_classes[i]]}\n", flush=True)

