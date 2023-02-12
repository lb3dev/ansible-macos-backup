backup:
		ansible-playbook playbook-backup.yml --tags "backup" --extra-vars "@config.yml"

check:
		ansible-playbook playbook-backup.yml --tags "check" --extra-vars "@config.yml"

all:
		ansible-playbook playbook-backup.yml --extra-vars "@config.yml"

bw:
		ansible-playbook playbook-bitwarden.yml --extra-vars "@config.yml"

firefox:
		ansible-playbook playbook-firefox.yml --extra-vars "@config.yml"

test:
		ansible-playbook tests/test.yml

test-all:
		ansible-playbook tests/playbook-test.yml

lint:
		yamllint .
