# install libs
# devtools::install_github("tidyverse/tidyverse")
# devtools::install_github("r-lib/httr") # send HTTP requests and receive responses

# load libs
library(tidyverse)
library(httr)


# Azure Backend
end.point <- "https://people-counter.cognitiveservices.azure.com/"
key1 <- readChar("key.txt", file.info("key.txt")$size)

