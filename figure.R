args <- commandArgs(TRUE)
filename <- args[1]
print(paste("Filename is: ", filename, sep=""))

x = c(-1, 0, 1)
png(filename)
plot(sin(x))
dev.off()
