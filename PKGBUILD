pkgname=phx-font-metrics
pkgver=2.0.0
pkgrel=1
pkgdesc="Extract metrics from a TTF font file for generating a custom Material You typescale."
arch=("x86_64" "aarch64")
url="https://github.com/andreapeverelli/phx-font-metrics.git"
license=('GPL-3.0')

makedepends=(
	"python"
	"python-pip"
)

options=(!debug)

build() {
	mkdir -p ../bin
	mkdir -p ../.venv/phx-font-metrics
	python -m venv ../.venv/phx-font-metrics/
	source ../.venv/phx-font-metrics/bin/activate
	pip install fonttools brotli nuitka
	python -m nuitka --onefile --standalone --output-filename=../bin/phx-font-metrics main.py
}

package() {
	install -dm755 "$pkgdir/usr/share/$pkgname"
	cp ../LICENSE $pkgdir/usr/share/$pkgname
	install -Dm755 ../bin/phx-font-metrics $pkgdir/usr/bin/phx-font-metrics
}
