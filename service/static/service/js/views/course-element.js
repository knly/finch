var app = app || {};

app.CourseElement = Backbone.View.extend({
		className: '',

		template: _.template(`This is a variable of template <%=variations %>
	<div class="container">
 
    		<h3>Tabs -left</h3>      		
      		<div class="row variwrapper">
 				<div class="col-sm-3 varibrowsing">
			        <ul class="nav nav-pills nav-stacked">
			        <% for (var variation of variations){ %>
			          <li class="nav-item"><a href="#a"  class="nav-link active" data-toggle="tab"><%=variation.description %><span class="varidelete" id="<%=variation.id %>">x</span></a></li>
			        <% } %>
			        <li class="nav-item"><a href="#add"  class="nav-link variadd"><span>+</span></a></li>
			        </ul>
			    </div>
			    <div class="col-sm-9 varicontentholder">
			        <div class="tab-content varicontent">
			        	 <% for (var variation of variations){ %>
				         <div class="tab-pane active" id="<%=variation.id %>"><%=variation.content %></div>
				         <% } %>
			    	</div>
			   	</div>
		    </div>
    </div>
      
    </div></div>`),

		initialize: function(options) {
		 	_.extend(this, _.pick(options,'variations'));
			
		},

		render: function(){
			this.$el.html(this.template({ variations: this.variations }));
			return this;
		},

		events: {
			'click .variadd':'addvari',
		},

		addvari: function(event){
			//variations.push
		},
});