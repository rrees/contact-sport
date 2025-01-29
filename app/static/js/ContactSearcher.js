export class ContactSearcher extends HTMLElement {
	connectedCallback() {

		const searchResultsElement = this.querySelector('#contact-search-results');

		const searchBox = this.querySelector('[name="name"]');

		function handleSearch(event) {
			event.preventDefault();

			const formData = new FormData(event.target);

			event.target.disabled = true;
			searchBox.disabled = true;

			const apiUrl = `/directory/${formData.get('directory-id')}/find-contacts/by-name/${formData.get('name')}`;
			console.log(apiUrl);
			fetch(apiUrl).then((response) => {

				// console.log(response);

				response.text().then((responseHtml) => {
					searchResultsElement.innerHTML = responseHtml;
				});
			}).finally(() => {
				event.target.disabled = false;
				searchBox.disabled = false;
			});
		}

		this.querySelector('.search-form').addEventListener('submit', handleSearch);
	}
}

customElements.define('contact-searcher', ContactSearcher);