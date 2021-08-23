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

<main>
  <h1>IJMES Transliterator</h1>
  <textarea bind:value={text} rows="3" />
  <button on:click|preventDefault={handleSubmit}>Transliterate</button>
  <div>
    {#if result}
      <p>{result}</p>
    {/if}
  </div>
</main>

<style>
  textarea {
    display: block;
  }
</style>
