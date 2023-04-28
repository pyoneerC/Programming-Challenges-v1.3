from random import normalvariate # returns float

print(normalvariate(5, 10))
print(normalvariate(1, 10))
print(normalvariate(1, 10))
print(normalvariate(1, 10))
print(normalvariate(1, 10))
print(normalvariate(1, 10))

# 1 is mu, 10 is sigma. Mu means average value, and sigma the variation, so (1,40) will give us any number, while (5,5) will give 5.0, therefore (5,6) will give around 5. Bigger the sigma, more random the number, If the value of mu is less than the value of sigma, it means that the mean or average value of the distribution is less than the standard deviation or the spread of the distribution. In such a case, the majority of the data points will be concentrated around the mean, and there will be fewer points further away from the mean. The distribution will be more narrow and peaked, and less spread out.

# 13.66919857468568
# -15.903254597719187
# -26.616322546130863
# 10.880718076166026
# 0.19648799235383785
# 8.957545503653733

# Generates a float of 16 decimals