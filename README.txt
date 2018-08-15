PRE-REQUISITES:
Ansible, python36, open_cv module, RHEL7

SETUP STEPS:
1)Copy 10-custom.rules to /etc/udev/rules.d/
2)copy photo_mail to your desktop
3)Create an ansible-vault secret.yml file which consists of : password: (your password)
inside the photo_mail folder. Delete the existing secret.yml file before doing so.
4)Enter your vault password in vault_pass file
5)Enter your email ID in the mentioned places in web.yml
6)Write : ansible-playbook /root/Desktop/photo_mail/onboot.yml --vault-password-file=/root/Desktop/photo_mail/vault_pass
  in your /root/.bashrc file

YOU'RE GOOD TO GO!