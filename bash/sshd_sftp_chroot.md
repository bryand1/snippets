[Restrict SSH User Access to Certain Directory using Chrooted Jail](https://www.tecmint.com/restrict-ssh-user-to-directory-using-chrooted-jail/)

## Create SSH Chroot Jail

1. Start by creating the chroot jail using the mkdir command below:

```bash
mkdir -p /var/uploads
```

2. Identify the required files to support a user's session. For an interactive session, this requires at least a shell `/bin/bash` and basic `/dev` nodes such as null, zero, stdin, stdout, stderr, and tty devices:

```bash
ls -l /dev/{null,zero,stdin,stdout,stderr,random,tty}
```

3. Create the `/dev` files as follows using the `mknod` command. The command below, the `-m` flag is used to specify the file permissions bits, `c` means character file and the two numbers are major and minor numbers that the file points to.

```bash
mkdir -p /var/uploads/dev/
cd /var/uploads/dev
mknod -m 666 null c 1 3
mknod -m 666 tty c 5 0
mknod -m 666 zero c 1 5
mknod -m 666 random c 1 8
```

4. Set permissions. The chroot jail and its subdirectories and subfiles must be owned by root user and not writable by any normal user or group

```bash
chown root:root /var/uploads
chmod 0755 /var/uploads
ls -ld /var/uploads
```

## Setup Interactive Shell for SSH Chroot Jail

5. First, create the `bin` directory and then copy the `/bin/bash` files into the `bin` directory as follows:

```bash
mkdir -p /var/uploads/bin
cp -v /bin/bash /var/uploads/bin
```
6. Now, identify bash required shared `libs`, as below and copy them into the `lib` directory

```bash
ldd /bin/bash
mkdir -p /var/uploads/lib64
cp -v /lib64/{libtinfo.so.5,libdl.so.2,libc.so.6,ld-linux-x86-64.so} /var/uploads/lib64
```

## Create and Configure SSH User

7. Now, create the SSH user with the `useradd` command 

```bash
useradd bryanandrade
```

8. Create the chroot jail general configurations directory, `/var/uploads/etc` and copy the updated account files (*etc/passwd* and *etc/group*) into this directory as follows:

```bash
mkdir /var/uploads/etc
cp -vf /etc/{passwd,group} /var/uploads/etc
```

9. Now, open the `sshd_config` file.

```bash
vi /etc/ssh/sshd_config
```

and modify/add these lines to the _bottom_ of the file

```bash
# define username to apply chroot jail to
Match User bryanandrade
# specify chroot jail
ChrootDirectory /var/uploads
```

Save the file and exit, and restart the SSHD services:

```bash
systemctl restart sshd
```

## Testing SSH with Chroot Jail

10. At this point, test if the chroot jail setup is working as expected:

```bash
ssh bryanandrade@192.168.100.2
```

The SSH user is locked in the chrooted jail and can't run any external commands(`ls`, `date`, `uname`, etc).

The user can only execute bash and its builtin commands such as (`pwd`, `history`, `echo`, etc) as seen below:

```bash
ssh bryanandrade@192.168.100.2
pwd
echo "Test"
history
```

## Create SSH User's Home Directory and Add Linux Commands

11. Create a home directory for the SSH user like so (do this for all future users)

```bash
mkdir -p /var/uploads/home/bryanandrade
chown -R bryanandrade:bryanandrade /var/uploads/home/bryanandrade
chmod -R 0700 /var/uploads/home/bryanandrade
```

12. Next, install a few user commands such as `ls`, `date`, `mkdir` in the `bin` directory

```bash
cp -v /bin/ls /var/uploads/bin
cp -v /bin/date /var/uploads/bin
cp -v /bin/mkdir /var/uploads/bin
```

13. Check the shared libraries for the commands above and move them into the chrooted jail libraries directory:

```bash
ldd /bin/ls
cp -v /lib64/{libselinux.so.1,libcap.so.2,libacl.so.1,libc.so.6,libpcre.so.1,libdl.so.2,ld-linux-x86-64.so.2,libattr.so.1,libpthread.so.0} /var/uploads/lib64/
```

## Testing SFTP with Chroot Jail

14. Do a final test using sftp; check if the commands you have just installed are working.

Add the line below in the `/etc/ssh/sshd_config` file:

```bash
# Enable sftp to chrooted jail
ForceCommand internal-sftp
```

```bash
systemctl restart sshd
```

15. Test using SSH and you will get the following error

```bash
ssh bryanandrade@192.168.100.2
# This service allows sftp connections only.
# Connection to 192.168.100.2 closed.
```

Try using SFTP as follows

```bash
sftp -i /path/to/keyfile bryanandrade@192.168.100.2
```

[How to make files created in a directory owned by directory group](https://superuser.com/questions/102253/how-to-make-files-created-in-a-directory-owned-by-directory-group)

`chmod g+s directory`
