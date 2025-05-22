SRC := $(shell find . -name "*.java")
OUT := out
MAIN_CLASS := lab3.adapter.Demo

.PHONY: all clean run

all: compile

compile:
	mkdir -p $(OUT)
	javac -d $(OUT) $(SRC)

run: compile
	java -cp $(OUT) $(MAIN_CLASS)

clean:
	rm -rf $(OUT)
