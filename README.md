# Task 1 Software configuration
## Subtask1: Why did I choose to participate in the challenge portfolio?

**Hello, world! 😊** 

I decided to take part in the project because I want to try my hand at QA. Due to the events in Ukraine, my field has become irrelevant, so I really want to learn a new direction that will be interesting and relevant. In addition, I am driven by the desire to provide for my family.

My main goal is to complete my studies, get an internship and achieve good results already in the coming year.

From the project, I expect ~~treats :)~~ to understand the basics of QA, get a chance to continue this work and to have an interesting time.

And yes, thank you for this opportunity 🙌

                                                 MAX SLAVIANSKY
# Task 2 Selectors

## Subtask1: Searching for selectors on the login pageList all the elements that are on the login page.

* **Scouts panel**

//*[@id="__next"]/form/div/div[1]/h5

//*[text()="Scouts Panel"]

//child::div/h5

* **Remind Password**

//*[@id="__next"]/form/div/div[1]/a

//*[text()="Remind password"]

//child::div/a

* **Login**

//*[@id="login"]

//*[text()="Login"]

#login

* **Password**

//*[@id="password"]

//*[text()="Password"]

#password-label


* **SIGN IN**

//*[text()="Sign in"]

//*[contains(@class, "MuiButton")]

//*[@id="__next"]/form/div/div[2]/button

* **Language**

//*[@id="__next"]/form/div/div[2]/div/div

/html/body/div[1]/form/div/div[2]/div/div

#__next > form > div > div.MuiCardActions-root > div > div