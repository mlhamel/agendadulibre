ifndef message
	message = "Updating web app"
endif

ifndef repos
	repos = mlhamel/agendadulibre
endif

.SHELLFLAGS = -e
.PHONY: docker-build
.NOTPARALLEL:

default: build
build: docker-build
commit: docker-commit
push: docker-push
docker-build: do-docker-build
docker-commit: do-docker-commit
docker-push: do-docker-push

do-docker-build:
	docker build -t agendadulibre --no-cache --rm . | tee build.log || exit 1

do-docker-commit:
	docker commit -m $(message) $(revision) $(repos)

do-docker-push:
	docker push $(repos)

# Version Bump using bumpversion
patch:
	bumpversion patch
major:
	bumpversion major
minor:
	bumpversion minor