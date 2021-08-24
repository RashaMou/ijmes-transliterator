<script>
  import axios from "axios";
  export let text;
  let result;

  async function handleSubmit() {
    const res = await axios.post("http://localhost:5001/transliterate", {
      text,
    });
    result = res.data;
    text = "";
  }
</script>

<header>
  <h1>IJMES Transliterator</h1>
</header>
<main>
  <textarea dir="rtl" bind:value={text} rows="5" />
  <button on:click|preventDefault={handleSubmit}>Transliterate</button>
  <div>
    {#if result}
      <p>{result}</p>
    {/if}
  </div>
</main>
<footer>Diacritization powered by Farasa. No relation to IJMES.</footer>

<style>
  :global(body) {
    background-color: #d3cec8;
  }

  header {
    margin-bottom: 70px;
    /* max-width: 50rem; */
    /* background-color: #fac6b8; */
  }
  main {
    background-color: #edecea;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 300px;
    max-width: 50rem;
    margin: 0 auto;
    border-radius: 3px;
    box-shadow: 0 1px 1px rgba(0, 0, 0, 0.15), 0 2px 2px rgba(0, 0, 0, 0.15),
      0 4px 4px rgba(0, 0, 0, 0.15), 0 8px 8px rgba(0, 0, 0, 0.15);
  }
  h1 {
    text-align: center;
    color: #1c3554;
    color: #cf7351;
  }
  textarea {
    display: block;
    outline: none;
    resize: none;
    border-radius: 3px;
    width: 40rem;
    margin: 50px 0 20px 0;
  }
  button {
    border-radius: 3px;
    width: 30%;
    background-color: #abd9ce;
    color: #1c3554;
  }

  button:hover {
    background-color: #1c3554;
    color: #abd9ce;
  }

  footer {
    margin-top: 100px;
    color: #cf7351;
  }
</style>
