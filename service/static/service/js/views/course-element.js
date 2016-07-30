var app = app || {};

app.CourseElement = Backbone.View.extend({
		className: '',

		template: _.template(`
	<div class="container">
 
    		<h3>Tabs -left</h3>      		
      		<div class="row variwrapper">
 				<div class="col-sm-3 varibrowsing">
			        <ul class="nav nav-pills nav-stacked">
			        <% for (var variation of variations){ %>
			          <li class="nav-item"><a href="#div<%=variation.id %>" id="li<%=variation.id %>" class="nav-link" data-toggle="tab"><span contenteditable><%=variation.description %></span><span class="varidelete" id="del<%=variation.id %>">x</span></a></li>
			        <% } %>
			        <li class="nav-item"><a href="#add"  class="nav-link variadd"><span>+</span></a></li>
			        </ul>
			    </div>
			    <div class="col-sm-9 varicontentholder">
			        <div class="tab-content varicontent">
			        	 <% for (var variation of variations){ %>
				         <div class="tab-pane editme" id="div<%=variation.id %>"><%=variation.content %></div>
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
			this.variations.push({id:this.variations.length+1,content:"You created a new variation of a course.",description:"New Variation"});
			this.render();
		},
});