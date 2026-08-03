pkgname=phx-font-metrics
pkgver=1.0.0
pkgrel=1
pkgdesc="Generates CSS font-metrics that fits the Google Sans typescale of Material You"
arch=('any')
url="https://github.com/andreapeverelli/phx-font-metrics.git"
license=('GPL-3.0')

depends=(
	'python'
	'python-pip'
)

build() {
	python -m venv ../.venv/phx-font-metrics/
	source ../.venv/phx-tonal-palette/bin/activate
	pip install coloraide nuitka
	python -m nuitka --onefile --standalone --output-filename=../bin/phx-font-metrics main.py
}

package() {
	install -dm755 "$pkgdir/usr/share/$pkgname"
	cp ../LICENSE $pkgdir/usr/share/$pkgname
	install -Dm755 ../bin/phx-font-metrics $pkgdir/usr/bin/phx-font-metrics
}
