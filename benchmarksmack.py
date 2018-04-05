import docker
import argparse

dockerImage = 'grubb/smack-docker'

def test_toy(timelimit):
	client = docker.from_env()
	client.images.pull(dockerImage)
	container = client.containers.run(dockerImage, detach=True, volumes={''})
	print "Benchmarking with LAVA toy has not been implemented"

def test_1(timelimit):
	print "Benchmarking with LAVA-1 has not been implemented"

def test_M(timelimit):
	print "Benchmarking with LAVA-M has not been implemented"


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Benchmark SMACK against pieces of the LAVA corpora')
	parser.add_argument('--lavaset', default='toy', choices=['toy', '1', 'M'], help='LAVA dataset to analyze [default: toy]')
	parser.add_argument('--time-limit', dest='timelimit', default=1200, type=int, help='Time limit of each smack run in seconds. [default: 1200]')

	args = parser.parse_args()
	
	if args.lavaset == "toy":
		test_toy(args.timelimit)
	elif args.lavaset == "1":
		test_1(args.timelimit)
	elif args.lavaset == "M":
		test_M(args.timelimit)