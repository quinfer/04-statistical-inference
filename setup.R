library(ggplot2)
library(rstanarm)
profbeautyeval <- read_csv("/home/quinfer/R/rethinking-econometrics/course-material/slides/04-statistical-inference-simulation/profbeautyeval.csv")
options(mc.cores = parallel::detectCores())
m1<-stan_glm(eval~beauty,data=profbeautyeval,algorithm='optimizing')
saveRDS(m1,"bayesmodel.rds")
profbeautyeval %>%
  ggplot(aes(y=beauty,x=eval)) +
  geom_point() +
  labs(x="student evaluation (standardised)",y="prof beauty (student estimates)") +
  geom_smooth(method = "lm",se=FALSE) ->g1
ggplot2::ggsave(g1,width = 12,height=8,filename = "/home/quinfer/R/rethinking-econometrics/course-material/slides/04-statistical-inference-simulation/img/beauty.png")
