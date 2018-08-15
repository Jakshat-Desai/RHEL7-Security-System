#!/usr/bin/python36

import subprocess

subprocess.getoutput("ansible-playbook /root/Desktop/photo_mail/web.yml --vault-password-file=\"/root/Desktop/photo_mail/vault_pass\"")
