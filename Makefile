backup:
		ansible-playbook playbook-backup.yml --extra-vars "@vault" --ask-vault-pass

test:
		ansible-playbook playbook-backup.yml --extra-vars "@tests/test-vault" --ask-vault-pass

test-setup:
		ansible-playbook tests/playbook-test-setup.yml
