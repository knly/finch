var app = app || {};

app.CourseElement = Backbone.View.extend({
		className: '',

		template: _.template('This is a variable of template <%=content%>'),

		initialize: function(options) {
			_.extend(this, _.pick(options,'content'));
		},

		render: function(){
			this.$el.html(this.template({ content: this.content }));
			return this;
		},
});