# EVA: Security Framework

## What is EVA?

EVA is a Security Framework for Linux and Im building a Device for it wich would Connect to the Security Framework and show the stats/alerts/ directly onto the screen without looking at a terminal. the Design is inspired by the MAGI system of Evangelion. It would show on the OLED Screen about the Ads the Firewall blocked and the trackers destroyed. when someone is attacking a network whether by a DDOS attack or anything else. it would show a RED ALERT on the Screen. there would be a Button on the device which would remove the access to internet from the computer. The Security Framework is designed by my other teammate tho, its a really good defense system for Linux Nerds and Paranoid People. Since this thing runs in the background and you must be tech savy to understand whats happening, I'm building this device which would make it understand to lower life forms. 

Today I worked on the Schematic a little bit, I looked up the Components I would need to build this and everything else. I picked RP2040 because its very powerful and really great microcontroller, I also added the mandatory Flash and LDO regulator. a bunch of resistors and capacitors and USB C. I Worked on the Schematic for 3-4 hours and here's the result:

![](/Schematics/Schematic-2.png)

The way it works is by getting data from USB from the computer or device running the framework and showcases it onto the OLED screen. And it is inspired from the MAGI system, which are basically 3 supercomputers, who each check and find the best option of the situation by basically conversing. This Concept is sooooo peak and people have made quiet alot of project from this concept so ours won't be the first.

Im going to work on the CAD for now. Worked on the CAD a little bit, Still alot of work left for it to be finished, im so tired and cooked man, I want the device to be like those device that show some kind of status etc and are mostly on the table but for cybersecurity. My friend mostly worked on the software side and im on the hardware side, After working again on software for a bit i have realised that ts ain't for me. I like Hardware way more and its more fun as well. I worked on the CAD and this is the result:

![](/CAD/CAD.png)

I like it as of now, but its far from finished. I'll work more on it in the next week Insha-Allah. Im so tired tho. Next I have to work on the PCB and the Evangelion Aesthetic more, and also the GUI of Framework. Im not really on the Software side tho so other guy will most likely work on that. We were three people but the 3rd guy won't make it, and im skeptical by the other guy too. Im not even sure about myself If ill be able to get 10 hours. BUT IM NOT GONNA GIVE UP. I MUST DO IT BECAUSE 1000$ IS ON THE LINE.

Zyinc will add more security things to the framework like a privacy layer which sits in-between the browser and computer, every trafic that comes from the browser will be filtered and only white-listed stuff will be allowed and the everything that is on the black-list will be removed. This is called a Firewall, this is a game-changer because alot of these popular companies try to sell data and what not by using trackers etc, which is absolutely riducolous. This firewall will protect you from that. People say that I have nothing to hide whatsoever but thats like saying idk about freedom of speech because i have nothing to say which is sooo dumb. Don't be like this and Actually Save yourself from these companies which exploit your data.

 This Framework also includes VPN which is completely free btw. now you'll say how's that possible but it is. there's a thing Called NAT which zyinc will use to give you guys free VPN, cmon what more do you want.

 But thats not IT, it also has DNS filtering. DNS is basically a phonebook. when you search google.com on the web, it first looks at the DNS and if the address is written on it, you'll reach the website. Normally everything works out of the box, the DNS is provided by Your ISP. but you can Change it to whatever you want. Some Examples are cloudflare DNS which is pretty good as well. Idk which Zyinc is going to use tho. DAMN, i yap so much when it comes to this stuff.

 Well this is it for today i guess. Next week i'll lock in from the start and won't procrastinate. Insha-Allah.