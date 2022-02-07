backup:
		ansible-playbook playbook-backup.yml --extra-vars "@vault" --ask-vault-pass

test:
		ansible-playbook tests/playbook-test.yml
