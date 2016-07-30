var app = app || {};

app.CourseElement = Backbone.View.extend({
		className: '',

		template: _.template(`This is a variable of template <%=content%>
	<div class="container">
 
    		<h3>Tabs -left</h3>      		
      		<div class="row">
 				<div class="col-sm-3">
			        <ul class="nav nav-pills white nav-stacked">
			          <li class="nav-item"><a href="#a"  class="nav-link active" data-toggle="tab">One</a></li>
			          <li class="nav-item"><a href="#b"  class="nav-link" data-toggle="tab">Two</a></li>
			          <li class="nav-item"><a href="#c"  class="nav-link" data-toggle="tab">Twee</a></li>
			        </ul>
			    </div>
			    <div class="col-sm-3">
			        <div class="tab-content">
				         <div class="tab-pane active" id="a">Lorem ipsum dolor sit amet, charetra varius quam sit amet vulputate. 
				         Quisque mauris augue, molestie tincidunt condimentum vitae, gravida a libero.</div>
				         <div class="tab-pane" id="b">Secondo sed ac orci quis tortor imperdiet venenatis. Duis elementum auctor accumsan. 
				         Aliquam in felis sit amet augue.</div>
				         <div class="tab-pane" id="c">Thirdamuno, ipsum dolor sit amet, consectetur adipiscing elit. Duis pharetra varius quam sit amet vulputate. 
				         Quisque mauris augue, molestie tincidunt condimentum vitae. </div>
			    	</div>
			   	</div>
		    </div>
    </div>
      
    </div></div>`),

		initialize: function(options) {
			_.extend(this, _.pick(options,'content'));
		},

		render: function(){
			this.$el.html(this.template({ content: this.content }));
			return this;
		},
});