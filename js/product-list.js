// product-list.js

// Tạo danh sách file ảnh tự động từ Code_sofa_1 đến Code_sofa_64
const imageFiles = [];
for (let i = 1; i <= 64; i++) {
  imageFiles.push(`Code_sofa_${i}.jpg`);
}

// Dữ liệu sản phẩm tương ứng
const products = imageFiles.map((img, index) => ({
  name: `Sofa Model ${index + 1}`,
  brand: `Luxury Sofa`,
  price: `Liên hệ`, // Giá mỗi mẫu tăng 10$
  img: img,
  detailUrl: 'sofa-single.html'
}));

// Hàm render sản phẩm
function renderProducts(containerId) {
  const container = document.getElementById(containerId);
  if (!container) {
    console.error(`Không tìm thấy element với id "${containerId}"`);
    return;
  }

  container.innerHTML = products.map(product => `
    <div class="col-md-4">
      <div class="car-wrap rounded ftco-animate">
        <div class="img rounded d-flex align-items-end" style="background-image: url(${product.img});">
        </div>
        <div class="text">
          <h2 class="mb-0"><a href="${product.detailUrl}">${product.name}</a></h2>
          <div class="d-flex mb-3">
            <span class="cat">${product.brand}</span>
            <p class="price ml-auto">${product.price} <span>/item</span></p>
          </div>
          <p class="d-flex mb-0 d-block">
            <a href="#" class="btn btn-primary py-2 mr-1">Order now</a>
            <a href="${product.detailUrl}" class="btn btn-secondary py-2 ml-1">Details</a>
          </p>
        </div>
      </div>
    </div>
  `).join('');
  console.log('Images:', imageFiles);
}
