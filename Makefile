backup:
		ansible-playbook playbook-backup.yml --tags "backup" --extra-vars "@vault" --ask-vault-pass

test:
		ansible-playbook tests/playbook-test.yml --tags "backup"

edit:
		ansible-vault edit vault
