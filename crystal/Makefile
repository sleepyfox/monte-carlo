.PHONY: run test

run:
	docker run -it -v `pwd`:/var/app/project sleepyfox/crystal sh

test:
	docker run -it -v `pwd`:/var/app/project sleepyfox/crystal crystal spec --verbose
