x  <-  c(1,2,3,4,5)
x


x <- c('A','B','C','가','나','다')
x

class(x)

x <- c('1','2','3')

x <- '2018-01-18'
class(x)

x <- as.Date('2020-1-18')
x
class(x)

y <- as.Date('2019-1-18')
class(y)
x - y

x <- TRUE
y <- FALSE
class(x)
class(y)

x <- c(1,2,'a',4)
x
x[2] # R은 1에서 시작한다.

x[3]

x[c(2,3)]

x[2:3]

x[-1]
x[x=='a']

x <- factor(c('M','F','F','M'))
levels(x)

levels(x) <- c('A','B')
x

x <- matrix(1:20, 5,4)

class(x)

