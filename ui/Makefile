all: scss

scss:
	scss --sourcemap=none scss/styles.scss styles.css

clean:
	rm styles.css
	rm -r .sass-cache*

.PHONY: clean, scss
