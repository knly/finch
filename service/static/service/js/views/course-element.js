var app = app || {};

app.CourseElement = Backbone.View.extend({
		className: '',

		template: _.template(`
	<div class="container">  		
      		<div class="row variwrapper">
 				<div class="col-sm-3 varibrowsing">
			        <ul class="nav nav-pills nav-stacked">
			        <% for (var variation of variations){ %>
			          <li class="nav-item"><a href="#div<%=variation.id %>" id="li<%=variation.id %>" class="nav-link" data-toggle="tab"><span contenteditable><%=variation.description %></span><span class="varidelete" id="<%=variation.id %>">x</span></a></li>
			        <% } %>
			        <li class="nav-item"><a href="#add"  class="nav-link variadd"><span>+</span></a></li>
			        </ul>
			    </div>
			    <div class="col-sm-9 varicontentholder">
			        <div class="tab-content varich">
			        	 <% for (var variation of variations){ %>
				         <div class="tab-pane editme varicontent" id="div<%=variation.id %>"><%=variation.content %></div>
				         <% } %>
			    	</div>
			   	</div>
		    </div>
    </div>
    <div>&nbsp;</div><hr>
      
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
			'click .varidelete':'remvari',
		},

		addvari: function(event){
			this.variations.push({id:this.variations.length+5,content:"You created a new variation of a course.",description:"New Variation"});
			this.render();
		},

		remvari: function(event){
			var ident = event.target.id;
			//console.log(ident);

			var index=0;

			for (var variation of this.variations){
				if(variation.id == ident){
					if (index > -1){
						this.variations.splice(index, 1);
					}
					break;
				}
				index++;
			}

			this.render();
		},
});