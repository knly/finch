var app = app || {};

app.MultipleChoiceQuestionElement = Backbone.View.extend({
		className: '',

		template: _.template('HELLO WORLD'),

		initialize: function(options) {
			_.extend(this, _.pick(options,'content'));
		},

		render: function(){
			this.$el.html(this.template({ content: this.content }));
			return this;
		},
});