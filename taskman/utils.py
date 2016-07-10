import re

def make_title_case(s):
	articles = ['a', 'an', 'of', 'the', 'is']

	word_list = re.split(' ', s)		#	re.split behaves as expected

	final = [word_list[0].capitalize()]	#	First word is always to be capitalised,
										#	even if it is an article
	for word in word_list[1:]:

		final.append(word in articles and word or word.capitalize())

	return " ".join(final)