import docker
import argparse
import os

dockerImage = 'grubb/smack-docker'

def test_toy(timelimit):
	client = docker.from_env()
	dir_path = os.path.dirname(os.path.realpath(__file__))
	container = client.containers.run(dockerImage, detach=True, volumes={dir_path + '/toy_example_distrib': {'bind': '/toy', 'mode': 'rw'}})
	(exit_code, output) = container.exec_run(['smack', '--only-check-valid-deref', '/toy/buggy/2/toy/toy.c'])
	print exit_code
	print output
	container.stop()
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