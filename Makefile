backup:
		ansible-playbook playbook-backup.yml --extra-vars "@backups.yml"

test:
		ansible-playbook playbook-backup.yml --extra-vars "@tests/test.yml"

test-setup:
		ansible-playbook tests/playbook-test-setup.yml
