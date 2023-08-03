/**
 * Take an HTML string and convert it to a live HTML element.
 * 
 * This returns the element(s) themselves, and can be manipulated as such
 * 
 * The string must have a single parent (no siblings on the highest level, eg how react does it)
 * 
 * @param htmlString eg: "\<p class="myClass" id="myID"\>\</p\>"
 * @returns HTML Element (or null if the string parses to no HTML elements)
 */
export function render( htmlString: string ): Node
{
  const elements = new DOMParser().parseFromString( htmlString, "text/html" ).body.children

  if ( elements.length > 1 ) throw new Error( "ADSU | HTML String cannot have siblings!" )
  if ( elements.length < 1 ) throw new Error( "ADSU | HTML String must have an element!" )
  
  return elements[0] as Node
}