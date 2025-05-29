import React from 'react';
import Image from 'next/image';
import Link from 'next/link';
import { motion } from 'framer-motion';
import workflowMarkdown from '../data/workflow_markdown';
import styles from '../styles/Home.module.css';

export default function Home() {
  React.useEffect(() => {
    // Initialize Mermaid diagrams
    const script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js';
    script.async = true;
    script.onload = () => {
      if (typeof window.mermaid !== 'undefined') {
        window.mermaid.initialize({ startOnLoad: true });
      }
    };
    document.body.appendChild(script);

    return () => {
      document.body.removeChild(script);
    };
  }, []);

  // Convert markdown to HTML
  const workflowHtml = workflowMarkdown
    .replace(/```mermaid/g, '<div class="mermaid">')
    .replace(/```/g, '</div>')
    .replace(/# /g, '<h2>')
    .replace(/## /g, '<h3>')
    .replace(/### /g, '<h4>')
    .replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2">$1</a>')
    .replace(/- \[(.*?)\]/g, '<li>$1</li>');

  return (
    <div className={styles.container}>
      <main className={styles.main}>
        <h1 className={styles.title}>
          Clean Tech CRM & AI Automation
        </h1>

        <div className={styles.workflow}>
          <div className={styles.workflowDiagram}>
            <div className="mermaid">
              {workflowMarkdown}
            </div>
          </div>

          <div className={styles.documentation}>
            <h2>Workflow Documentation</h2>
            <div dangerouslySetInnerHTML={{ __html: workflowHtml }} />
          </div>
        </div>
      </main>
    </div>
  );
}
