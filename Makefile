backup:
		ansible-playbook playbook-backup.yml --tags "backup" --extra-vars "@vault" --ask-vault-pass

check:
		ansible-playbook playbook-backup.yml --tags "check" --extra-vars "@vault" --ask-vault-pass

all:
		ansible-playbook playbook-backup.yml --tags "backup,check" --extra-vars "@vault" --ask-vault-pass

test:
		ansible-playbook tests/test.yml --skip-tags "check"

test-all:
		ansible-playbook tests/playbook-test.yml --skip-tags "check"

edit:
		ansible-vault edit vault
