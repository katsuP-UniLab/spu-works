const menu = document.querySelector("#menu");

menu.innerHTML = `<nav class="navbar navbar-expand-lg navbar-dark gradient-bg">
<div class="container-fluid">
  <a class="navbar-brand" href="/week7"><img src="https://suphakit.net/favicon.png" style="width: 30px; aspect-ratio: 1/1;" alt=""></a>
  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
      <li class="nav-item">
        <a class="nav-link active" aria-current="page" href="/week7">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/week7/product">Product</a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
          Dropdown
        </a>
        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
          <li><a class="dropdown-item" href="#">Action</a></li>
          <li><a class="dropdown-item" href="#">Another action</a></li>
          <li><hr class="dropdown-divider"></li>
          <li><a class="dropdown-item" href="#">Something else here</a></li>
        </ul>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#" tabindex="-1">About Us</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/week7/contact" tabindex="-1">Contact</a>
      </li>
    </ul>
    <form class="d-flex">
      <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success text-light border-2" type="submit">Search</button>
    </form>
  </div>
</div>
</nav>`;
