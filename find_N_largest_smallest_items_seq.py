import heapq

def find_N_largest_items_seq(seq, N):
	return heapq.nlargest(N,seq)

def find_N_smallest_items_seq(seq, N):
	return heapq.nsmallest(N, seq)