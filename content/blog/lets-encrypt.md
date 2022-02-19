Title: Let's get Encrypted!
Date: 2022-02-14 20:20:54+00:00
Entry-ID: 2
UUID: ed4cc531-305f-5088-b49f-4bf16030704a

I'm running SSL now! *clicks button* "That was easy..."

.....

I suppose this is a minor update, and was planned since I first though to set this up, but *dang* has certbot gotten easier to use.

To be fair, last time I set it up was with an unofficial build on a Windows IIS server, but I remember needing to manually set up directories for certbot to place acme challenge data, having to manually edit configs, and handle task scheduling and restarting the daemon.

These days it's two commands:

```
sudo snap install --classic certbot
sudo certbot --nginx
```

And I didn't even have to worry about my reverse proxy setup or anything! Thanks EFF!
