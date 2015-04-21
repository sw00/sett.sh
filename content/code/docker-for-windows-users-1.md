Title: Docker for Windows Users Part I
Slug: docker-for-windows-users-1
Date: 2015-04-21
Modified: 2015-04-21
Tags: docker, devops, tools
Summary: I've seen a lot of developers either unaware and confused as to what exactly Docker and containerisation is all about. This is because they have either never encountered the use case for it, or primarily work in Windows environments. With these blog series, I'll try and explain what all the fuss is about and hopefully how you can use it in your little way.

### Foreword

I won't actually be teaching you how to use Docker in this first post, - this one is just to explain where it all fits in. I'm also using this opportunity to explain Linux and its importance/relevance. If you want a TL;DR introduction read this [StackOverflow question](http://stackoverflow.com/questions/16047306/how-is-docker-io-different-from-a-normal-virtual-machine).

As with many people my age (27), I primarily started working and playing on computers when graphical user interfaces were already the norm and Windows 95 had just hit the peak of popularity. Unless your parents were engineers of some sort, personal computers were generally seen as just a new home appliance. If you had a computer in the 90s, it most likely was a Packard Bell that came with Windows 95 and Intel Pentium processor of some sort.

![Packard Bell Pentium 133](http://i.imgur.com/7hVG709.jpg)<br/>
<small>Low-res nostalgia bomb!</small>

It's in this context that a lot of us grew up. However, this puts us at a disadvantage. Just as today's "apps", tablets and smart phones can be seen as relegating the general purpose computer to "Facebook" machines, ours was the first wave of this trend. The capacitive touch screen is just the evolution of the computer mouse. This is a great thing, but if you're a technologist, it's important to understand that the Windows ecosystem is only one alternate timeline in the history of computing.

Below, I'll go through a brief history of computing that's important to understanding why you'd want to be familiar with *nix. Especially if you're from the Windows 95 generation, like me. Bear with me as I dig through the alternate history, I'm trying to give you the same _ah-ha!_ moments I got when I first discovered this stuff.

### In the beginning
In the beginning there was UNIX. Before affordable multi-purpose, personal computers, organisations often kept a single mainframe computer that users could connect to via ["dumb" terminals](https://en.wikipedia.org/wiki/Computer_terminal#Dumb_terminals). This was based on the idea of [time-sharing](https://en.wikipedia.org/wiki/Time-sharing) which was a way to give access to computing to many different people at the same time[^internet].

![Tron Classic](http://i.imgur.com/lYUYMUG.jpg)
<br/><small>A lot the original computing ideas are realised in [Tron (1982)](http://www.imdb.com/title/tt0084827/), albeit with artistic liberties taken.</small>

UNIX as an underlying operating system provided small programs that the user could execute in order to specific tasks. These were tied together by a unified file system for communicating and a shell scripting language for doing more complex work. All of this work was mediated by a master control program, the [kernel](https://en.wikipedia.org/wiki/Kernel_(operating_system)).

Eventually in the 80s, the IEEE got together and specified a family of standards for operating systems based on common patterns they saw in UNIX and UNIX-like OSes. They called these standards collectively, [POSIX](https://en.wikipedia.org/wiki/POSIX). Parallel to this, a set of common software engineering practices were embodied into something called the [Unix Philosophy](https://en.wikipedia.org/wiki/Unix_philosophy).

A lot of operating systems would come to be developed adhering to POSIX standards and and the Unix philosophy. The most famous of them being Linux[^linux] and FreeBSD[^OSX].

![Unix timeline](https://upload.wikimedia.org/wikipedia/commons/c/cd/Unix_timeline.en.svg)

### MS-DOS & Windows

In 1981 IBM launched the IBM Personal Computer with a microprocessor based on its flagship 8088 chip[^8088]. It also came installled a with tiny, simple operating system by Microsoft, called MS-DOS. Unlike UNIX-like operating systems around at the time, MS-DOS was single-task, single-user and certainly not POSIX compliant.

![MS-DOS box](http://i.imgur.com/0Z1RcIAl.jpg)

Personal computers became insanely popular for some reason and Microsoft introduced Windows as an addon to MS-DOS to compete with Apple's very expensive Macintosh computer. The Macintosh featured a Graphical User Interface, the hottest new thing in technology. The rest is history: Windows dominated the personal computing space through OEM deals with hardware manufacturers and eventually every computer you could buy was either a Windows or a Mac. Meanwhile, UNIX-like OSes like Linux took firm hold of the Web Server space. The numbers are very [telling](https://en.wikipedia.org/wiki/Usage_share_of_operating_systems#Market_share_by_category): 91.25% of all personal computers are Windows, but only a third of servers on the web.

### Implications

What does this mean for us developers? Well, unless you're strictly into systems development[^systems development] only, the chances are you'll be developing applications that need to deployed to a server. This means that 2 of 3 production environments will UNIX-like.

### Virtualisation

Because a server rack is a specialised, expensive piece of equipment, a common technique to have a more efficient distribution of resources is to use [virtualisation](https://en.wikipedia.org/wiki/Hardware_virtualization). Virtualisation in the context of the data centre allows sharing the same physical resources amongst multiple instances of virtual servers. 

Apart from efficiency, virtualisation provides other benefits such as the ability to easily automatically configure them. New virtual machines can be "spun up" and provisioned without buying additional hardware up-front. You can clone/back up entire machines and move them around. These are all features that are the backbone for Infrastructure as a Service (IaaS) which simply means you can pay a provider like [Rackspace](http://rackspace.com/), [Linode](https://www.linode.com/) or [Digital Ocean](https://www.digitalocean.com/) for a Virtual Private Server and have it almost immediately.

![Virtualisation diagram](https://www.vmware.com/files/images/diagrams/vmw-virtualization-defined.jpg)
<small>VMWare explains virtualisation.</small>

The most common scenario for virtualisation is on a hardware level: the host machine's physical resources would be virtualised and available to the guest machine as "fake" hardware. Physical things like RAM, CPU, GPU and HDD could be virtualised. A host machine with 32GB RAM, 1TB HDD and 8 CPUs could possible provide 4 virtual machines of 8GB, 250GB and 2 vCPU. The problem however, is that these resources are fixed for the duration that the VM is running - if 1 VM is idle, it can't share its 2vCPUS and 8GB RAM with the others. Also, each VM would need to boot up and run its own OS. This is still a little inefficient.

With regards to software development, virtualisation allows us to easily have consistent environments amongst locally through the use of [vagrant](http://vagrantup.com/) and virtual box.

### Containers

Containers are just another term for [Operating System Level Virtualisation](https://en.wikipedia.org/wiki/Operating-system-level_virtualization). In contrast to whole-system or hardware virtualisation, containers do not provide abstraction for physical resources. Instead, they provide a virtual userspace[^userspace] and directory structure for applications to be run. These applications all run on the same operating system and kernel but are isolated from each other. One application in a container would generally not be able to see or manipulate files/memory in another container.

Operating System Level Virtualisation ala containers has a massive advantage over hardware virtualisation in that you can easily run hundreds of containers on a host without any problems since they share all physical resources of the host system.

![Containers vs VMs](http://zdnet4.cbsistatic.com/hub/i/r/2014/10/02/c5ebe949-49e6-11e4-b6a0-d4ae52e95e57/resize/770x578/54eff63621dfffda68806c80e2a411a5/azuredockervmcontainer.png)

The reason why containers are not very prominent in Windows ecosystem is because of its single-user, single-process history (I stand to be corrected on this). Also containerisation was never a core operating system feature and traditionally provided by third party, proprietary software in Windows.

On Linux, [chroot](https://en.wikipedia.org/wiki/Chroot) had always provided this functionality until [Linux Containers](https://wiki.archlinux.org/index.php/Linux_Containers)(LxCs) were created in 2008. LxCs leveraged a kernel feature called **cgroups** to achieve a higher level of isolation adn security than what the crude chroot provided[^cgroups].

If the previous paragraph is kind of hard to take in, you're not alone. Containerisation in Linux is a highly technical topic and it seems to require a lot of arcane knowledge of the Linux operating systems that most developers wouldn't know of. Let alone devs who are used to Windows. This was always the case until **Docker** exploded on to the scene.

### Docker
Docker was started by [Solomon Hykes](https://twitter.com/solomonstre) in 2013 while he was at [dotCloud](https://www.dotcloud.com/), a Platform as a Service Provider[^PaaS]. It was initially just a convenient wrapper around LxCs that stretched the metaphor of "shipping containers" for apps. The entire idea was that a docker container should run and look exactly the same on any host while being incredibly easy to automate and manage.

One distinctive feature docker has is that it uses the AUFS filesystem which is a layered file system. This simply means that AUFS can take a base image of filesystem and apply changes to it and each change will have it's own unique layer. In practice this is effectively source control built into the file system, with additional features of being able to mount other filesystems into paths in it.

Another benefit is that it allows you to run applications for any Linux distribution on the same host. Since it effectively allows you to define the userspace/userland filesystem, you can deploy an app or service in a CentOS container and it will run just fine on an Ubuntu host for example.

More recently, Microsoft has actually developed a docker container for [ASP.NET](https://registry.hub.docker.com/u/microsoft/aspnet/) so you can now deploy your .NET applications on a Linux host, or [vice-versa](http://weblogs.asp.net/scottgu/docker-and-microsoft-integrating-docker-with-windows-server-and-microsoft-azure).


### What's in it for Devs?

Just like Vagrant changed the way we provision and develop applications, Docker is the next step to solving the problem of "well, it works on my machine". Using Docker, you can now have an multi-service environment that is almost exactly like production running on your local machine. 

With [micro-services](http://www.thoughtworks.com/insights/blog/microservices-nutshell) gaining popularity, we're going to see a lot of software complexity pushed from away from dev effort and into the ops realm. But in order to remain effective devs, we're going to have care a lot more about how our code is deployed and lives in production. This partially what the **DevOps** movement is all about. Being able to deploy and run our entire application locally, make changes and trust that it will behave the same way in all stages is a massive win for developers and operations folk alike.

I've used docker to provide a local development environment for an app that consumed 7 individual services. By packaging each one into separate containers and then bundling them into a single vagrant box that can be fired up through a [go script](http://www.thoughtworks.com/insights/blog/praise-go-script-part-i). Sadly, we never got around to using it production but it greatly aided the production support and feature development.

It turns out Docker is also an extremely useful tool when dealing with critical database migrations. I've used it to create a snapshot of a production database and test migrations locally. Fortunately, it was small enough. Because of its underling AUFS filesystem, rolling back meant I simply could kill the container and firing it up again would revert it to its initial state.

### End

I hope that this post has been helpful and gives you an idea of where docker fits in and how it came about. In the next post I'll explain how to get started with Docker and get our hands dirty. Cheers.


[^internet]: these principles would lay the foundation of computer interaction that we now call The Internet.

[^linux]: Linux needs no introduction but it was an attempt at making an operating system that was free, unlike UNIX which only massive organisations could afford.

[^OSX]: OSX is actually based off of BSD!

[^8088]: the 8088's predecessor is the 8086, which the term x86 architecture comes from.

[^systems development]: You know, like C, C++, Golang and Rust where knowing about memory management is more important than REST/SOAP calls and HTTP.

[^userspace]: also known as userland, it's the context in which non-kernel programs and drivers are run. I'm unaware if Windows has the equivalent architecture. [Read more](https://en.wikipedia.org/wiki/Operating-system-level_virtualization)

[^cgroups]: I won't go into more technical detail here, mostly because I don't know much about cgroups other than you can use it to limit memory and CPU resources to users and groups. See [https://wiki.archlinux.org/index.php/Cgroups](https://wiki.archlinux.org/index.php/Cgroups) for more info.

[^PaaS]: Remember IaaS? PaaS is the same thing but instead of spinning up VMs with specified RAM, vCPUs and HDD you work with spinning up services like Apache, MySQL, MongoDB, Logstache with ports, credentials and loadbalancing directly.