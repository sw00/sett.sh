+++
date = "2015-04-15"
title = "Contributing to Pixelated"
tags = ["code", "open source", "security"]
aliases = [ "/post/contributing-to-pixelated/" ]

+++

Last week the pixelated team here in TW Porto Alegre hosted a hack night which allowed me to dive into the enigmatic [Pixelated Project](https://pixelated-project.org/) and even submit a pull request! Read on if you'd like to know more.

The majority of the world's emails are hosted at large, centralised providers. Let's face it, there is practically no substitute for Gmail and in light of the Snowden Revelations we've willingly sacrificed our privacy for convenience. Pixelated aims to provide a secure alternative that everyone can use.

#Architecture

Pixelated consists of two major components, namely the Pixelated [User Agent](https://github.com/pixelated-project/pixelated-user-agent) and the [LEAP Platform](https://github.com/pixelated-project/leap_platform)[^1]. 

The User Agent is practically a conventional web application that acts as your mail client. It consists of a really lightweight UI built with Foundation CSS framework and [FlightJS](https://github.com/flightjs/flight)[^2]. For the back-end it's using [Twisted](https://twistedmatrix.com/trac/), the infamous asynchronous web framework for Python. This acts as the backbone for sending and receiving emails from providers (hosts), either over plain old SMTP or [soledad](https://leap.se/soledad) if your provider is a LEAP Platform.


# Get it, run it

The Pixelated team has made it as easy as possible for anyone who'd like to dive in and contribute. I'm also really impressed by the progress they've made in just 9 months.

You're going to need:

1. Git
2. Vagrant & Virtualbox

You'll want to clone the user agent repository from github into a directory of your choice:

`git clone https://github.com/pixelated-project/pixelated-user-agent.git`

There is a `Vagrantfile` that will provision a local development environment for you. Be warned however, it will first download the LEAP base box from [https://downloads.leap.se/platform/vagrant/virtualbox/leap-wheezy.box](https://downloads.leap.se/platform/vagrant/virtualbox/leap-wheezy.box) if you don't have it already. If you're unconcerned, just run:

`vagrant up`

Once the box is up, it also will provision it with Puppet - I had to do this several times because Puppet will still run even if there are failures. If you're curious as to what puppet is doing, have a look in the `provisioning/` directory.

Provisioning will take almost 20 minutes so while that's happening, head on over to the Pixelated dev provider at [https://dev.pixelated-project.org/](https://dev.pixelated-project.org/) and sign up for an account.

Once the box has been provisioned you'll need to run the go script[^3] which will setup the npm and (bower)[http://bower.io/] side of things: 

    vagrant ssh
    cd service
    ./go setup
    
Now, just one more step to get it running. The user agent needs to connect to a provider that you've registered with. In traditional terms, this is meant to be your ISP's mail server, Gmail, company's Exchange server...except this is a Pixelated provider. 

To fire up the user agent, just type the command below and follow the prompts. Be sure to enter `dev.pixelated-project.org` as the host and ensure your path to the certificate is correct. I had trouble initially because I had typos in my path that I didn't find.

`pixelated-user-agent --host 0.0.0.0 -lc /vagrant/service/pixelated/certificates/dev.pixelated-project.org.ca.crt`


# Contribute

The team has [a few dozen issues](https://github.com/pixelated-project/pixelated-user-agent/issues?q=is%3Aopen+is%3Aissue+label%3ABeginners) on github tagged with **Beginner** label to encourage contributions from newbies. Simply pick one and dive right in, the problems range from changing icons to exposing some property via RESTful API. So great little pieces of work that can take less than 3 hours to complete (what's more interesting is that it allows you get to know the codebase better)

I found the project really easy to get into and just getting your first pull request to be accepted feels awesome. I would highly recommend getting involved with Pixelated Project, not only does it have a great, fun tech stack with pieces for anyone, it's also a high impact social project. 

I can easily see this being used in by organisations internally instead of the poorly supported Gmail for Enterprise. Wouldn't it be great to free yourself from Gmail but keep all the functionality and have an even better UI? Not to mention the security benefits.

[^1]: I think a lot of the focus will be on the User Agent, since the LEAP platform will be implementation specific and is well supported by the [https://leap.se/](LEAP Foundation) already. Although I did hear something about developing ability for  infrastructure to fire up docker containers for each User Agent's session (!! way too cool)

[^2]: FlightJS is an extremely basic JS library that gives you the event emitter/subscriber pattern. This is great because it allows you build your app interaction any way you'd like without buying into a whole framework's way of doing things.

[^3]: A go script is that script in every software project that is the central point to trigger tasks such as setting up the environment, database migrations, build and run tests. It just has a name now: the `./go` script.
