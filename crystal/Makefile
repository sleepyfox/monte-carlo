.PHONY: run test format

run:
	docker run -it -v `pwd`:/var/app/project sleepyfox/crystal crystal run src/run_simulation.cr

sh:
	docker run -it -v `pwd`:/var/app/project sleepyfox/crystal sh

test:
	docker run -it -v `pwd`:/var/app/project sleepyfox/crystal crystal spec --verbose

format:
	docker run -it -v `pwd`:/var/app/project sleepyfox/crystal crystal tool format spec/monte_carlo_spec.cr
