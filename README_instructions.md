# Data Scientist Recruitment Challenge

## Introduction

Hi there!

Great news - if you're reading this it means that we believe that you have
what it takes to become the newest member of our team! Of course, as
data-centric professionals we cannot just trust our gut. Hence, we have created
this challenge to test your mettle.

What do you need to prove to us? A lot - but certainly the following:

1. You are self reliant
2. You know how to use data tools
3. You have a healthy dose of common sense
4. You can present results with your audience in mind
5. You have some creativity / originality in your style of problem solving

## Your mission
As a new member of our team you have been presented with a dataset from
a new customer. This customer is a retailer who sells shoes across multiple
shops, both online and offline. They want us to tackle a problem that a lot of
retailers face: products being returned. As the retailer (due to market demand)
offers free order shipping on online sales and free return shipping on both online
and offline sales, a high number of return can have a dramatic impact. As a
rough estimation, the retailer tells you that shipping a product (both orders and
return).

As with most data science projects, there are three main challenges within this
project to be tackled. We expect you to work out (at least) one of these in-depth,
while (at least) briefly touching upon the two others, with e.g., a proposed road
map. Not all parts should be tackled in the same way, some work best in a
notebook, others could benefit from slides or even some deployed code somewhere
online. Don't forget to play to your strengths! Pick the part where you can
astonish us the most! The three main challenges are:

1. **Maths & Statistics**: Modelling, understanding and predicting:
Given the datasample that you received, can you detect relevant structures
in this data? What is driving these returns? Can you predict returns?
How would you define a relevant prediction? How good do you consider
your model and why? What would you need to further improve these
predictions? Note that we don't indicate what exactly should be predicted,
just that it should somehow teach us something relevant about returns.

2. **Business understanding & value creation**: Given a predictive model
that tells us something about returns, what can we do with this? What
would you consider a good model? How can we make it actionable? What are the risks involved? How will we monitor performance? What gains can
be expected?

3. **Data engineering, deployment & usability**: Given a well-enough
performing predictive model and a proven business case, how will you
make it operationable and usable? Where does the solution live? How can
it be (safely) used by stakeholders? Where does the data live and how
(and when?) does it get there? How would you tackle and manage further
development?

## The data
You have received a data sample that you can use when designing your solution.
Note that this dataset is based on real data, but has been manipulated in such a
way that it cannot be traced back to any original source. As such, some things
might look like gibberish, but we are convinced that you will find a way to
work with it anyway. It does, however, contain enough "real" relationships and
structure to be considered similar enough to an actual dataset for purpose of
this exercise. Each of the lines contains info on the sale of a single product. The
meaning of most of the columns should be obvious. Keep in mind that the "true"
info is masked. This means that, e.g., the _ModelGroup_ "high heels" might be
encoded as "3162564956579801398".

Some extra notes:

- _Returned_ indicates if the product of this particular sale has eventually
been returned (1) or not (0).
- Shops with a three digit number (100 and above) are webshops.
- _SaleDocumentNumber_ indicates a basket of products. As such, lines with
the same _SaleDocumentNumber_ can be considered as bought together.
If you are unsure about something - feel free to make assumptions, but, as always,
mention this in your presentation.

## Deliverables
As the newest team member you are expected to take the first steps towards
solving this case for this client. We want you to show us a walkthrough of your
code/notebooks /. . . Focus on the important aspects - no need to show us how
you load the data. What solution techniques would you plan on using? Why?
Imagine this to be presented to the tech lead of your project, someone who
has substantial experience and will challenge you on the technical and business
aspects of what you propose. As such, you can assume that the person that
will receive your solution has as much Data Science knowledge as you have.
As mentioned beforehand, we expect you to tackle (at least) one of the three
challenges in-depth.

Note that as a next step in the recruitment process, if we are convinced by your
work, we will ask you to give a brief presentation where you present your findings
to a management audience. There, you will have to defend your business case.
Imagine this to be a dry-run with the product owner from our side (= the person
responsible for taking the client's perspective) or with stakeholders from the
retailer. This presentation doesn't have to be finished in this step, but you can
already keep it in the back of your mind.

#### Important note
While we want you to show us what you've got,
there is no need to fully "solve" the case; no need to create every
single possible model and deploy everything on a server. Focus on
the important part: show how you would solve things, convince us
that you understand what you are doing.

**As a closing argument please include how you would approach
this if you had had more time, and how much more
time you would expect to need to perform the additional
things you have in mind.**

Impress us! Good luck!