all: scss jsx

scss:
	scss --sourcemap=none scss/styles.scss styles.css

jsx: build
	jsx src/ build/

build:
	mkdir build;

clean:
	-rm -r build
	-rm styles.css
	-rm -r .sass-cache*

.PHONY: scss jsx clean
