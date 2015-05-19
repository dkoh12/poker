def shuffle(deck):
	"Knuth's Algorithm P"
	N = len(deck)
	for i in range(N-1):
		swap(deck, i, random.randrange(i, N))

def swap(deck, i, j):
	"swap elements i and j of a collection"
	print 'swap', i, j
	deck[i], deck[j] = deck[j], deck[i]
	

def test_shuffler(shuffler, deck='abcd', n=10000):
	counts = defaultdict(int)
	for _ in range(n):
		input = list(deck)
		shuffler(input)
		counts[''.join(input)] += 1
	e = n*1./factorial(len(deck))  ##expected count
	ok = all((0.9 <= counts[item]/e <= 1.1) for item in counts)
	name == shuffler.__name__
	print '%s(%s) %s' % (name, deck, ('ok' if ok else '*** BAD ***'))
	print '    ',
	for item, count in sorted(counts.items()):
		print "%s:%4.1f" % (item, count*100./n),
	print

def test_shufflers(shufflers=[shuffle, shuffle1], decks=['abc','ab']):
	for deck in decks:
		print
		for f in shufflers:
			test_shuffler(f, deck)

def factorial(n): return 1 if (n <= 1) else n*factorial(n-1)
