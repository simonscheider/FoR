#install.packages("readxl")
library("readxl")
#install.packages("wordcloud") # word-cloud generator
library("wordcloud")
#stevenson <- read_excel("Stevenson_assessment.xlsx", sheet = "Tabelle1")
stevenson <- read_excel(file.choose())
framecount = table(stevenson$'1', stevenson$zonal)


H <- apply(framecount, 2L, cumsum) - framecount / 2
bp <- barplot(framecount,
     main="Plot of frame types detected in Stevenson's 'Kidnapped'",
     xlab = "frame types",
     ylab = "frequency",
     col = c('dark grey','white')
     #rownames(framecount)
     )
text(rep(bp, each = nrow(H)), H, labels = ifelse(framecount == 0, "", framecount))

legend("topleft", legend = c('False', 'True'), fill = c('dark grey','white'))


wordcount = table(stevenson$at[stevenson$'1'==0], stevenson$zonal[stevenson$'1'==0]) 

wordcount = wordcount[order(wordcount$zonal),]

wordcount_df = data.frame(rbind(wordcount))

#barplot(wordcount[,c('zonal')])

set.seed(1234)
dev.new(width = 1000, height = 1000, unit = "px")
wordcloud(words = rownames(wordcount_df), freq = wordcount_df$zonal, min.freq = 1,
          max.words=200, random.order=FALSE, rot.per=0.35
          , colors=brewer.pal(8, "Dark2")
          )

