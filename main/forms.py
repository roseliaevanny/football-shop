from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "thumbnail", "category", "is_featured", "stock"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
    
    # {% if review %}
    #     <div class="review-container">
    #         {% for rev in review %}
    #             <div class="review-card">
    #                 <h2 class="review-product-name">{{ rev.product.name }}</h2>
    #                 <img class="review-product-image" src="{{ rev.product.image }}" alt="Product image">
    #                 <p class="review-product-price">{{ rev.product.price }}</p>
    #                 <p>{{ rev.date }}</p>
    #                 <h3 class="review-message">{{ rev.message }}</h3>
    #                 <div class="rating">
    #                     {% for i in 1|to:5 %}
    #                         <span class="star {% if i <= rev.rating %}rated{% endif %}">&#9733;</span>
    #                     {% endfor %}
    #                 </div>
    #             </div>
    #         {% endfor %}
    #     </div>
    # {% else %}
    #     <h2>No reviews yet.</h2>
    # {% endif %}