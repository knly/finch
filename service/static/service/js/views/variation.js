var app = app || {};

app.VariationView = Backbone.View.extend({
		className: '',
		
		template: _.template(``),

		initialize: function(options) {
			_.extend(this, _.pick(options,'content'));
		},

		render: function(){
			this.$el.html(this.template({ content: this.content }));
			return this;
		},

		events: {
			'click .variadd':'addvari',
		},

		addvari: function(event){
			console.log(event);
		},
});